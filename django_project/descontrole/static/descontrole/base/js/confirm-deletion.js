$(document).ready(function () {
    var formToSubmit;
    $('.delete-btn').on('click', function () {
        formToSubmit = $(this).closest('form');
        $('#deleteConfirmationModal').modal('show');
    });

    $('#confirmDeleteBtn').on('click', function () {
        formToSubmit.submit();
        $('#deleteConfirmationModal').modal('hide');
    });
});