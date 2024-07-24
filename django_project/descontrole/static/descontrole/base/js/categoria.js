document.addEventListener('DOMContentLoaded', function () {
    var editModal = document.getElementById('editModal');
    editModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');
        var nome = button.getAttribute('data-nome');
        var descricao = button.getAttribute('data-descricao');

        var form = editModal.querySelector('form');
        var action = BASE_URL.replace('9999', id)
        form.action = action;

        document.getElementById('id_nome').value = nome;
        document.getElementById('id_descricao').value = descricao;
    });

    var deleteModal = document.getElementById('deleteModal');
    deleteModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var id = button.getAttribute('data-id');

        var form = deleteModal.querySelector('form');
        var action = DELETE_URL.replace('9999', id);
        form.action = action;
    });
});

document.getElementById('create-form').addEventListener('submit', function (event) {
    event.preventDefault();
    var form = event.target;
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 400) {
            location.reload();
        } else {
            try {
                var response = JSON.parse(xhr.responseText);
                document.getElementById('errorMessage').innerText = response.error;
                var errorModal = new bootstrap.Modal(document.getElementById('errorModal'));
                errorModal.show();
            } catch (e) {
                console.error('Failed to parse JSON response:', e);
            }
        }
    };
    xhr.send(formData);
});

document.getElementById('edit-form').addEventListener('submit', function (event) {
    event.preventDefault();
    var form = event.target;
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 400) {
            location.reload();
        } else {
            try {
                var response = JSON.parse(xhr.responseText);
                document.getElementById('errorMessage').innerText = response.error;
                var errorModal = new bootstrap.Modal(document.getElementById('errorModal'));
                errorModal.show();
            } catch (e) {
                console.error('Failed to parse JSON response:', e);
            }
        }
    };
    xhr.send(formData);
});

document.getElementById('delete-form').addEventListener('submit', function (event) {
    event.preventDefault();
    var form = event.target;
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', form.action, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 400) {
            location.reload();
        } else {
            try {
                var response = JSON.parse(xhr.responseText);
                alert('Erro ao deletar categoria: ' + response.error);
            } catch (e) {
                console.error('Failed to parse JSON response:', e);
            }
        }
    };
    xhr.send(formData);
});

$(document).ready(function () {
    $('#form-export').submit(function (event) {
        event.preventDefault();
        $.get($(this).attr('action'), function (response) {
            if (response.error_message) {
                $('#exportErrorMessage').text(response.error_message);
                $('#exportErrorModal').modal('show');
            } else {
                $('#form-export').unbind('submit').submit();
            }
        });
    });
});
