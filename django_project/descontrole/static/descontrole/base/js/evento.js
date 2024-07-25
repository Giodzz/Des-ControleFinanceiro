document.addEventListener('DOMContentLoaded', function () { // Placeholders
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


$(function () { // Calendar settings
    $('.datepicker').datepicker({
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
