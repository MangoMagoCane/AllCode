Satellite = Class{}

function Satellite:init()
    self.image = love.graphics.newImage('graphics/object.png')

    self.width = self.image:getWidth()
    self.height = self.image:getHeight()

    self.x = (VIRTUAL_WIDTH - self.width) / 2 - 20
    self.y = (VIRTUAL_HEIGHT - self.height) / 2
    self.y = self.y - VIRTUAL_HEIGHT/4

    self.center_x = self.x + self.width/2
    self.center_y = self.y + self.height/2

    self.mass = 5

    self.vel_x = 0
    self.vel_y = 0

    self.accel_x = 0
    self.accel_y = 0
end


function Satellite:update(dt)
    self.center_x = self.x + self.width/2
    self.center_y = self.y + self.height/2

    self.vel_x = self.vel_x + self.accel_x
    self.vel_y = self.vel_y + self.accel_y

    self.x = self.x + self.vel_x
    self.y = self.y + self.vel_y

end


function Satellite:render()
    love.graphics.draw(self.image, self.x, self.y, 0)
end