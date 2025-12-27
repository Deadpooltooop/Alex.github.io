// Эффект плавающего курсора
const cursor = document.querySelector('.cursor-follower');


document.addEventListener('mousemove', (e) => {
    cursor.style.left = `${e.clientX - 20}px`;
    cursor.style.top = `${e.clientY - 20}px`;
});

// Плавная загрузка изображений
document.querySelectorAll('img[loading="lazy"]').forEach(img => {
    img.addEventListener('load', () => {
        img.classList.add('loaded');
    });
});

// Открытие/закрытие мобильного меню
const burger = document.querySelector('.burger');
const nav = document.getElementById('main-nav');

burger.addEventListener('click', () => {
    nav.classList.toggle('active');
    burger.classList.toggle('active');
});
