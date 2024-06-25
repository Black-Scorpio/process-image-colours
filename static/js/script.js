var uploadedFilename = '';

$(document).ready(function () {
    $('#drop-area').on('dragover', function (e) {
        e.preventDefault();
        e.stopPropagation();
        $(this).addClass('dragging');
    });

    $('#drop-area').on('dragleave', function (e) {
        e.preventDefault();
        e.stopPropagation();
        $(this).removeClass('dragging');
    });

    $('#drop-area').on('drop', function (e) {
        e.preventDefault();
        e.stopPropagation();
        $(this).removeClass('dragging');
        var files = e.originalEvent.dataTransfer.files;
        handleFiles(files);
    });

    $('#drop-area').on('click', function () {
        $('#file-input').click();
    });

    $('#file-input').on('change', function () {
        var files = this.files;
        handleFiles(files);
    });

    $('#upload-btn').on('click', function () {
        $('#file-input').click();
    });

    function handleFiles(files) {
        if (files.length > 0) {
            var formData = new FormData();
            formData.append('file', files[0]);
            $('#progress').show();

            $.ajax({
                url: '/upload',
                method: 'POST',
                data: formData,
                contentType: false,
                processData: false,
                success: function (data) {
                    $('#progress').hide();
                    if (data.success) {
                        uploadedFilename = data.filename;
                        $('#uploaded-image').attr('src', data.image_url).show();
                        displayColors(data.colors);
                    }
                }
            });
        }
    }

    function displayColors(colors) {
        $('#colors').empty();
        $.each(colors, function (index, color) {
            var colorBox = $('<div class="color-box"></div>').css('background-color', color[0]);
            var colorLabel = $('<span></span>').text(color[0]);
            colorBox.append(colorLabel);
            $('#colors').append(colorBox);
        });
    }
});
