$(function () {
    $('#id_data').datepicker({
        dateFormat: "dd/mm/yy",
        duration: "fast",
        monthNames: [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ],
        monthNamesShort: [
            "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
            "Jul", "Ago", "Set", "Out", "Nov", "Dez"
        ],
        dayNames: [
            "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"
        ],
        dayNamesShort: [
            "Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"
        ],
        dayNamesMin: [
            "Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"
        ]
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const placeholders = {
        'categoria': 'Selecione uma categoria',
        'natureza': 'Selecione uma natureza',
        'tipo': 'Selecione um tipo'
    };

    function addPlaceholder(select, placeholderText) {
        if (select.options.length === 0 || select.options[0].value !== '') {
            const placeholderOption = document.createElement('option');
            placeholderOption.value = '';
            placeholderOption.text = placeholderText;
            placeholderOption.selected = true;
            placeholderOption.disabled = true;
            placeholderOption.hidden = true;
            select.insertBefore(placeholderOption, select.firstChild);
        }
    }

    document.querySelectorAll('select').forEach(select => {
        const placeholderText = placeholders[select.name];
        if (placeholderText) {
            addPlaceholder(select, placeholderText);
        }
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
            location.reload(); // Responsible for redirecting.
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

