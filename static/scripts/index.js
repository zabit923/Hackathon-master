const newsButton = document.getElementById('news_btn');
const titleNewsEl1 = document.getElementById('news_title_item1');
const newsTextEl1 = document.getElementById('news_text_item1');
const newsImg = document.getElementById('news_img');
const btn = document.getElementById('click_me');
let currentIndex = 0;
let data = [];

async function loadNewsData() {
  try {
    const response = await fetch('/get_news_data/');
    if (!response.ok) {
      throw new Error('Ошибка при загрузке данных');
    }
    data = await response.json();
    displayNews();
  } catch (error) {
    console.error(error);
  }
}

function displayNews() {
  if (currentIndex < data.length) {
    titleNewsEl1.innerText = data[currentIndex].titleNews;
    newsTextEl1.innerText = data[currentIndex].newsText;
    newsImg.src = data[currentIndex].image;

    const newsCreatedAt = new Date(data[currentIndex].Date);
    const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    const formattedDate = newsCreatedAt.toLocaleDateString('ru-RU', options);
    document.getElementById('news_created_at').innerText = `Дата выхода: ${formattedDate}`;

    currentIndex++;
  } else {
    currentIndex = 0;
    displayNews();
  }
}



btn.addEventListener('click', displayNews);

newsButton.addEventListener('click', () => {
  if (newsTextEl1.style.maxHeight) {
    newsTextEl1.style.maxHeight = null;
    newsButton.innerHTML = 'Подробнее';
  } else {
    newsTextEl1.style.maxHeight = newsTextEl1.scrollHeight + 'px';
    newsButton.innerHTML = 'Закрыть';
  }
});

loadNewsData();
