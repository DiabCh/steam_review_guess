
import logo from '../logo.svg';
import '../App.css';
import axios from 'axios';

const difficulties = [
    { name: 'Easy', value: 3 },
    { name: 'Normal', value: 4 },
    { name: 'Hard', value: 5 },
    { name: 'God Mode', value: 6}
  ];
function scrambleItems(game_list){
    let review_list
    let image_list

}


function createGameDiv(game_list){
    const main_container = document.createElement('div');
    main_container.classList.add('reviews_container');
    for (let element of game_list){
        let container = document.createElement('div');

        let imgElement = document.createElement('img');
        imgElement.src = element['header_image'];
        imgElement.className = 'game_img';
        container.appendChild(imgElement);

        let review = document.createElement('p');
        review.classList.add('review-text');
        review.textContent = element['review'];
        container.appendChild(review);
        main_container.appendChild(container);
    }
    return main_container

}

const handleDifficultyClick = (value) => {
    console.log(`Selected difficulty: ${value}`);
    document.getElementById('diff_sel').remove();
    document.getElementById('warning').innerHTML = 'Loading your Impending Doom'
    // Create container element


    axios.get('http://127.0.0.1:8000/games/random/reviews/?difficulty=' + value)
      .then(res => {
        console.log(res.data); 
        const game_list = JSON.parse(res.data);
        document.getElementById('warning').innerHTML =  'Select the corresponding reviews and images';
        let main_container = createGameDiv(game_list);
        console.log()
        document.getElementById('game').appendChild(main_container);
        }
        )


  };

function home(){

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div>
          <p id='warning'>
            Let's play a small game, choose a difficulty
          </p>
        </div>
        <div className='difficulty_selector' id='diff_sel'>

          {difficulties.map((difficulty) => (
            <button
              key={difficulty.value}
              type="button"
              className='button-34'
              onClick={() => handleDifficultyClick(difficulty.value)}
            >
              {difficulty.name}
            </button>
          ))}
        </div >
        <div id='game'></div>
      </header>
    </div>
  );
          }

export default home