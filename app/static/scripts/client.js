// Função para exibir o formulário correspondente
function showForm(event, type) {
    // Ocultar todos os forms
    document.getElementById('form-manual').classList.add('d-none');
    document.getElementById('form-csv').classList.add('d-none');
    document.getElementById('form-excel').classList.add('d-none');
    document.getElementById('form-paste').classList.add('d-none');

    // Exibir o formulário selecionado
    document.getElementById('form-' + type).classList.remove('d-none');

    // Remover cor de fundo de todos os botoes
    const buttons = document.querySelectorAll(".btn-select")

    for (let button of buttons) {
        button.classList.remove("btn-primary")
        button.classList.add("btn-outline-primary")
    }

    // Colocar cor azul no botao
    event.target.classList.remove("btn-outline-primary")
    event.target.classList.add("btn-primary")
}