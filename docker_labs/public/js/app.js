console.log('javascript is here')

const clickme = () => {
    let counter = document.getElementById('counter').textContent;
    counter = Number(counter) + 1;
    document.getElementById('counter').textContent = counter
}