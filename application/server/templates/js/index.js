class GameTile{
    constructor(parent_row_id, tile_id){
        // Create a new tile object
        // tile_id is a string
        this.tile_id = tile_id
        this.tile_value = ""
        $("#" + parent_row_id).append("<button id='"+ tile_id +"'class='guess-tile' disabled></button>")
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
    
}

function button_click(event) {
    button_value = event.currentTarget.value
    if(button_value == "ENTER" || button_value == "DELETE") {
        return
    }
    console.log(button_value)
}

$( document ).ready(function() {
    $("button").on("click", button_click)
    console.log( "ready!" );
    test = new GameBoard();
});