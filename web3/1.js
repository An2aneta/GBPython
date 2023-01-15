const tCels = Number.parseInt(prompt('Введите температуру в градусах Цельсия:'));
const tFar = Math.round((9 / 5 * tCels + 32) * 10)/10;
alert(`Цельсий: ${tCels}, Фаренгейт: ${tFar}`);