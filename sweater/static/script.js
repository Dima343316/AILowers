function convertToWords() {
    var numberInput2 = document.getElementById("numberInput2");
    var wordsOutput2 = document.getElementById("wordsOutput2");
    var numberInput3 = document.getElementById("numberInput3");
    var wordsOutput3 = document.getElementById("wordsOutput3");
    var numberInput4 = document.getElementById("numberInput4");
    var wordsOutput4 = document.getElementById("wordsOutput4");
    var numberInput5 = document.getElementById("numberInput5");
    var wordsOutput5 = document.getElementById("wordsOutput5");
    var number1 = parseInt(numberInput.value);
    var number2 = parseInt(numberInput2.value);
    var number3 = parseInt(numberInput3.value);
    var number4 = parseInt(numberInput4.value);
    var number5 = parseInt(numberInput5.value);
    var number6 = parseInt(numberInput6.value);
    var words = numberToWords(number1);
    var words2 = numberToWords(number2);
    var words3 = numberToWords(number3);
    var words4 = numberToWords(number4);
    var words5 = numberToWords(number5);
    var words6 = numberToWords(number6);
    wordsOutput.value = words;
    wordsOutput2.value = words2;
    wordsOutput3.value = words3;
    wordsOutput4.value = words4;
    wordsOutput5.value = words5;
    wordsOutput6.value = words6;
}

function convertToWords_run() {
    var numberInput = document.getElementById("numberInput");
    var wordsOutput = document.getElementById("wordsOutput");
    var numberInput6 = document.getElementById("numberInput6");
    var wordsOutput6 = document.getElementById("wordsOutput6");
    var number1 = parseInt(numberInput.value);
    var number6 = parseInt(numberInput6.value);
    var words = numberToWords(number1);
    var words6 = numberToWords(number6);
    wordsOutput.value = words;
    wordsOutput6.value = words6;
}

function numberToWords(number) {
  const units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять'];
  const teens = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'];
  const tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто'];
  const hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот'];
  const thousands = ['', 'тысяча', 'тысячи', 'тысяч'];
  const millions = ['', 'миллион', 'миллиона', 'миллионов'];
  const billions = ['', 'миллиард', 'миллиарда', 'миллиардов'];

  if (number === 0) {
    return 'ноль';
  }

  function convertThreeDigitNumber(num) {
    let result = '';

    const hundred = Math.floor(num / 100);
    const ten = Math.floor((num % 100) / 10);
    const unit = num % 10;

    if (hundred > 0) {
      result += hundreds[hundred] + ' ';
    }

    if (ten === 1 && unit > 0) {
      result += teens[unit] + ' ';
      return result.trim();
    } else if (ten > 0) {
      result += tens[ten] + ' ';
    }

    if (unit > 0) {
      result += units[unit] + ' ';
    }

    return result.trim();
  }

  let result = '';
  let numArr = [];

  if (number >= 1000000000) {
    const billion = Math.floor(number / 1000000000);
    numArr.push(convertThreeDigitNumber(billion));
    numArr.push(billions[getCorrectForm(billion)]);
    number %= 1000000000;
  }

  if (number >= 1000000) {
    const million = Math.floor(number / 1000000);
    numArr.push(convertThreeDigitNumber(million));
    numArr.push(millions[getCorrectForm(million)]);
    number %= 1000000;
  }

  if (number >= 1000) {
    const thousand = Math.floor(number / 1000);
    numArr.push(convertThreeDigitNumber(thousand));
    numArr.push(thousands[getCorrectForm(thousand)]);
    number %= 1000;
  }

  numArr.push(convertThreeDigitNumber(number));
  result = numArr.join(' ').trim();

  return result;
}

function getCorrectForm(number) {
  const lastDigit = number % 10;
  const secondToLastDigit = Math.floor((number % 100) / 10);

  if (secondToLastDigit === 1 || lastDigit === 0 || lastDigit >= 5) {
    return 3;
  } else if (lastDigit === 1) {
    return 1;
  } else {
    return 2;
  }
}