document.addEventListener('DOMContentLoaded', function(){
    let angry = document.querySelector(".angry");
    let funny = document.querySelector(".funny");
    let coquettish = document.querySelector(".coquettish");
    let sad = document.querySelector(".sad");
    let quest = document.querySelector(".quest");
    let neutral = document.querySelector(".neutral");
    let choice_block1 = document.querySelector(".choice_block1");
    let choice_block2 = document.querySelector(".choice_block2");
    let choice1 = document.querySelector(".choice1");
    let choice2 = document.querySelector(".choice2");
    angry.addEventListener('click', function(){
        funny.style.visibility = 'hidden';
        coquettish.style.visibility = 'hidden';
        sad.style.visibility = 'hidden';
        neutral.style.visibility = 'hidden';
        quest.innerHTML = "Спробувати вас розвеселити чи навалити криміналу?😕";
        choice_block1.style.visibility = 'visible';
        choice_block2.style.visibility = 'visible';
        choice1.value = "angry_1";
        choice2.value = "angry_2";
        choice1.innerHTML = "Розвеселити";
        choice2.innerHTML = "Кримінал";
    })
    funny.addEventListener('click', function(){
        angry.style.visibility = 'hidden';
        coquettish.style.visibility = 'hidden';
        sad.style.visibility = 'hidden';
        neutral.style.visibility = 'hidden';
        quest.innerHTML = "Щось веселе чи можливо хоррор?😨";
        choice_block1.style.visibility = 'visible';
        choice_block2.style.visibility = 'visible';
        choice1.value = "funny_1";
        choice2.value = "funny_2";
        choice1.innerHTML = "Веселе";
        choice2.innerHTML = "Хоррор";
    })
    coquettish.addEventListener('click', function(){
        funny.style.visibility = 'hidden';
        angry.style.visibility = 'hidden';
        sad.style.visibility = 'hidden';
        neutral.style.visibility = 'hidden';
        quest.innerHTML = "Тоді це романтика! 😘";
        choice_block1.style.visibility = 'visible';
        choice1.value = "coquettish_1";
        choice1.innerHTML = "Гаразд!";
    })
    sad.addEventListener('click', function(){
        funny.style.visibility = 'hidden';
        coquettish.style.visibility = 'hidden';
        angry.style.visibility = 'hidden';
        neutral.style.visibility = 'hidden';
        quest.innerHTML = "Посумуємо чи спробуємо розвеселитися?🥺";
        choice_block1.style.visibility = 'visible';
        choice_block2.style.visibility = 'visible';
        choice1.value = "sad_1";
        choice2.value = "sad_2";
        choice1.innerHTML = "Посумуємо";
        choice2.innerHTML = "Розвеселимось";
    })
    neutral.addEventListener('click', function(){
        funny.style.visibility = 'hidden';
        coquettish.style.visibility = 'hidden';
        sad.style.visibility = 'hidden';
        angry.style.visibility = 'hidden';
        quest.innerHTML = "Тоді довіртеся нашим алгоритмам!😉";
        choice_block1.style.visibility = 'visible';
        choice1.value = "neutral";
        choice1.innerHTML = "Гаразд";
    })
})
