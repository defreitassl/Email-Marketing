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

(function () {
    // Seleciona todos os formulários que queremos aplicar a validação
    var forms = document.querySelectorAll('.needs-validation');

    // Itera sobre eles e previne o envio caso o formulário seja inválido
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {

                // Seleciona os campos de entrada de categoria
                var categoryInput = document.getElementById('categoryInput');
                var categorySelect = document.getElementById('category');

                // Verifica se pelo menos um dos dois campos está preenchido
                if (!categoryInput.value && categorySelect.value === "Selecione uma categoria já registrada") {
                    event.preventDefault();
                    event.stopPropagation();
                    
                    // Adiciona uma mensagem customizada de erro
                    categoryInput.setCustomValidity("Preencha pelo menos um dos campos.");
                    categorySelect.setCustomValidity("Preencha pelo menos um dos campos.");
                } else {
                    // Remove a mensagem de erro se a validação for passada
                    categoryInput.setCustomValidity("");
                    categorySelect.setCustomValidity("");
                }

                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }

                form.classList.add('was-validated');
            }, false);
        });
})();
