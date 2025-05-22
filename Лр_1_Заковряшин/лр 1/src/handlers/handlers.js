import { Crypt } from '../encryption/Crypt_Rot_13.js';

export function initHandlers() {
  const input = document.getElementById('inputText');
  const output = document.getElementById('outputText');
  function updateEncryption() {
    output.value = Crypt(input.value).join('');
  }
  input.addEventListener('input', updateEncryption);
  updateEncryption();
}