from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Categoria
import pandas as pd


class CategoriaViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.categoria1 = Categoria.objects.create(
            nome="Categoria 1", descricao="Descrição da Categoria 1"
        )
        self.categoria2 = Categoria.objects.create(
            nome="Categoria 2", descricao="Descrição da Categoria 2"
        )

    def test_categoria_index(self):
        response = self.client.get(reverse("categoria_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "descontrole/categoria/index.html")
        self.assertIn("categorias", response.context)
        categorias = response.context["categorias"]
        self.assertEqual(list(categorias), [self.categoria1, self.categoria2])

    def test_categoria_create_valid(self):
        data = {"nome": "Nova Categoria", "descricao": "Descrição da Nova Categoria"}
        response = self.client.post(reverse("categoria_create"), data)
        self.assertRedirects(response, reverse("categoria_index"))
        self.assertEqual(Categoria.objects.count(), 3)

    def test_categoria_create_invalid(self):
        response = self.client.get(reverse("categoria_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "descontrole/categoria/form_invalido.html")

    def test_categoria_update_valid(self):
        data = {"nome": "Categoria Atualizada", "descricao": "Descrição atualizada"}
        response = self.client.post(
            reverse("categoria_update", args=[self.categoria1.id]), data
        )
        self.assertRedirects(response, reverse("categoria_index"))
        self.categoria1.refresh_from_db()
        self.assertEqual(self.categoria1.nome, "Categoria Atualizada")

    def test_categoria_update_invalid(self):
        data = {"nome": "", "descricao": "Descrição atualizada"}
        response = self.client.post(
            reverse("categoria_update", args=[self.categoria1.id]), data
        )
        self.assertRedirects(response, reverse("categoria_index"))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Não foi possível salvar a categoria.")

    def test_categoria_delete(self):
        response = self.client.post(
            reverse("categoria_delete", args=[self.categoria1.id])
        )
        self.assertRedirects(response, reverse("categoria_index"))
        self.assertFalse(Categoria.objects.filter(pk=self.categoria1.id).exists())

    def test_categoria_delete_ajax(self):
        response = self.client.post(
            reverse("categoria_delete", args=[self.categoria1.id]),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["success"], True)

    def test_categoria_delete_invalid(self):
        response = self.client.post(reverse("categoria_delete", args=[1000]))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["success"], False)

    def test_categoria_export(self):
        response = self.client.get(reverse("categoria_export"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/pdf")

    def test_categoria_export_no_items(self):
        Categoria.objects.all().delete()
        response = self.client.get(reverse("categoria_export"))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()["error_message"], "Nenhum item disponível para exportar."
        )
