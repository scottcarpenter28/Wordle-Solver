class GameTile{
    constructor(parent_row_id, tile_id){
        // Create a new tile object
        // tile_id is a string
        this.tile_id = tile_id
        this.tile_value = ""
        $("#" + parent_row_id).append("<button id='"+ tile_id +"'class='guess-tile' disabled></button>")
    }

    update_tile(){
        // Update the value of the tile
        $("#" + this.tile_id).text(this.tile_value);
        $("#" + this.tile_id).value = this.tile_value;
    }
}

class GameRow{
    constructor(row_id){
        // Create a new row object
        // row_id is a string
        this.row_id = "row_" + row_id
        this.tile_count = 5
        this.current_population = 0
        this.tiles = []
        $("#game-body").append("<div class='row game-row' id='" + this.row_id + "'></div>")
        for(let i=0; i<this.tile_count; i++){
            this.tiles.push(new GameTile(this.row_id, "tile_"+ i + "_" + this.row_id))
        }
    }

    set_tile_value(letter){
        // Set the value of the next available tile
        if(this.current_population >= this.tile_count)
            return console.error("Row is full");
        this.tiles[this.current_population].tile_value = letter;
        this.tiles[this.current_population].update_tile();
        this.current_population++;
    }

    remove_last_value(){
        // Remove the last value in the row
        this.current_population --;
        if(this.current_population < 0){
            this.current_population = 0;
            return console.error("Row is empty");
        }
        this.tiles[this.current_population].tile_value = "";
        this.tiles[this.current_population].update_tile();
    }
}

class GameBoard{
    constructor(){
        this.max_guesses = 6
        this.current_guess = 0
        this.board = []
        for(let i=0; i<this.max_guesses; i++){
            this.board.push(new GameRow(i))
        }
    }
    
    add_letter(letter){
        if(this.current_guess >= this.max_guesses)
            return console.error("Game is over");

        let current_row = this.board[this.current_guess];
        if(current_row.current_population >= current_row.tile_count)
            return console.error("Row is full");

        current_row.set_tile_value(letter);
    }

    delete_letter(){
        // Delete the last letter
        if(this.current_guess >= this.max_guesses)
            return console.error("Game is over");

        let current_row = this.board[this.current_guess];
        current_row.remove_last_value();
    }

    submit_guess(){
        // Submit the current guess
        if(this.current_guess >= this.max_guesses)
            return console.error("Game is over");

        this.current_guess++;
    }
}

function button_click(event) {
    button_value = event.currentTarget.value
    if(button_value == "ENTER")
        main_game.submit_guess();
    else if(button_value == "DELETE") 
        main_game.delete_letter();
    else
        main_game.add_letter(button_value);
}

let main_game;
function startup(){
    $("button").on("click", button_click)
    main_game = new GameBoard();
}

$( document ).ready(startup);