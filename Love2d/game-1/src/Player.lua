Player = Class{}

JERK = 1

function Player:init()
    self.image = love.graphics.newImage('graphics/angry-bird-icon.png')

    self.width = self.image:getWidth()
    self.height = self.image:getHeight()

    self.x = (VIRTUAL_WIDTH - self.width) / 2
    self.y = (VIRTUAL_HEIGHT - self.height) / 2

    self.dy = 0
    self.dx = 0

    self.accelx = 0
    self.accely = 0

    self.num = 1
end


function Player:update(dt)
    if love.keyboard.isDown('left') then
        self.accelx = self.accelx - JERK
    elseif love.keyboard.isDown('right') then
        self.accelx = self.accelx + JERK
    end

    if love.keyboard.isDown('down') then
        self.accely = self.accely + JERK
    elseif love.keyboard.isDown('up') then
        self.accely = self.accely - JERK
    end

    self.dx = self.dx + self.accelx * dt
    self.dy = self.dy + self.accely * dt

    self.x = self.x + self.dx * dt
    self.y = self.y + self.dy * dt
    
    if self.x <= 0 then
        self.x = 0
        self.accelx = -self.accelx
        self.dx = -self.dx
    elseif self.x >= VIRTUAL_WIDTH - self.width then
        self.x = VIRTUAL_WIDTH - self.width
        self.accelx = -self.accelx
        self.dx = -self.dx
    end


    if self.y <= 0 then
        self.y = 0
        self.accely = -self.accely
        self.dy = -self.dy
    elseif self.y >= VIRTUAL_HEIGHT - self.height then
        self.y = VIRTUAL_HEIGHT - self.height
        self.accely = -self.accely
        self.dy = -self.dy
    end

    if self.dx > 0 then
        self.accelx = self.accelx - self.num
    else
        self.accelx = self.accelx + self.num
    end

    if self.dy > 0 then
        self.accely = self.accely - self.num
    else
        self.accely = self.accely + self.num
    end
end


function Player:render()
    if self.dx >= 0 then
        self.sx = 1
        self.rendx = 0
    else
        self.sx = -1
        self.rendx = self.image:getWidth()
    end

    love.graphics.draw(self.image, self.x + self.rendx, self.y, 0, self.sx, 1)
end