document.addEventListener('DOMContentLoaded', function () {
    var botãoBody = document.querySelector('.botão-body');
    var botãoLinha = document.querySelector('.botão-linha');
    var menu = document.querySelector('.menu');

    botãoBody.addEventListener('click', function () {
        menu.classList.toggle('ativo');
        menu.classList.remove('ativo-reverse'); 
    });

    botãoLinha.addEventListener('click', function () {
        menu.classList.toggle('ativo-reverse');
        menu.classList.remove('ativo'); 
    });
});
