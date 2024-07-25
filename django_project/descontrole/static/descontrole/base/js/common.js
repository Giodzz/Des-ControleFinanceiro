document.addEventListener('DOMContentLoaded', function () {
    function setupModal(modalId, url) {
        var modal = document.getElementById(modalId);
        modal.addEventListener('show.bs.modal', function (event) {
            var button = event.relatedTarget;
            var id = button.getAttribute('data-id');
            var form = modal.querySelector('form');
            var action = url.replace('9999', id);
            form.action = action;

            var dataAttributes = button.dataset;
            for (var key in dataAttributes) {
                if (dataAttributes.hasOwnProperty(key)) {
                    var fieldId = 'id_' + key;
                    var input = document.getElementById(fieldId);
                    if (input) {
                        input.value = dataAttributes[key];
                    }
                }
            }
        });
    }
    setupModal('editModal', UPDATE_URL);
    setupModal('deleteModal', DELETE_URL);
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

// Export tables

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