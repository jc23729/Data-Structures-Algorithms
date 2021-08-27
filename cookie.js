// Classes is like a coookie cutter
// classes always have whats called a constructor

class Cookie {
    constructor(color) {
        this.color = color
    }
    // GETTERS
    getColor() {
        return this.color
    }
    // SETTERS
    setColor(color) {
        this.color = color
    }
}
//  we can create new cookies   
let cookieOne = new Cookie('green')
// its a specific instance of the class
let cookieTwo = new Cookie('blue')