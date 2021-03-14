var script = document.createElement("script");
script.type = "text/javascript";
script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";
document.head.appendChild(script);


script.onload = function() {
    tinymce.init({
        selector: '#id_content',

        menubar: false,
        toolbar: 'bullist, numlist',
        plugins: 'advlist',
        advlist_bullet_styles: 'square',
        advlist_number_styles: 'lower-alpha,lower-roman,upper-alpha,upper-roman'
    });
}