export default class vertice {
    constructor(x, y, name, color) {
        this.x = x
        this.y = y
        this.color = color
        this.name = name
        this.radious = 7
        this.around = 25
        this.moving = false
    }

    draw() {
        if (this.moving) {
            this.x = mouseX
            this.y = mouseY
            print('moving', this.name)
            fill('red')
            ellipse(this.x, this.y, this.radious * 2, this.radious * 2)


        }
        else {

            fill(this.color[0], this.color[1], this.color[2])
            ellipse(this.x, this.y, this.radious, this.radious)
        }

    }

    clicked(x, y) {
        let d = dist(x, y, this.x, this.y)
        if (d < this.around) {

            this.moving = !this.moving
        }
    }
}