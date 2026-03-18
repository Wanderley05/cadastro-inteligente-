const nome = document.getElementById('nome');
const email = document.getElementById('email');
const senha = document.getElementById('senha');
const confirmar = document.getElementById('confirmar');

nome.addEventListener('blur', validarNome);
email.addEventListener('blur', validarEmail);
senha.addEventListener('input', validarSenha);
confirmar.addEventListener('blur', validarConfirmar);

function erro(input, mensagem) {
  input.classList.add('error');
  input.classList.remove('success');
  document.getElementById(input.id + '-error').innerText = mensagem;
}

function sucesso(input) {
  input.classList.remove('error');
  input.classList.add('success');
  document.getElementById(input.id + '-error').innerText = "";
}

function validarNome() {
  if (nome.value.trim() === "") {
    erro(nome, "Nome obrigatório");
  } else if (nome.value.length < 3) {
    erro(nome, "Mínimo 3 caracteres");
  } else {
    sucesso(nome);
  }
}

function validarEmail() {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (email.value === "") {
    erro(email, "Email obrigatório");
  } else if (!regex.test(email.value)) {
    erro(email, "Email inválido");
  } else {
    sucesso(email);
  }
}

function validarSenha() {
  if (senha.value.length < 8) {
    erro(senha, "Mínimo 8 caracteres");
  } else if (!/[A-Z]/.test(senha.value)) {
    erro(senha, "Precisa de letra maiúscula");
  } else if (!/[0-9]/.test(senha.value)) {
    erro(senha, "Precisa de número");
  } else {
    sucesso(senha);
  }
}

function validarConfirmar() {
  if (confirmar.value !== senha.value) {
    erro(confirmar, "Senhas não coincidem");
  } else {
    sucesso(confirmar);
  }
}