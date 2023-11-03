Celestial = Class{}

function Celestial:init()
    self.image = love.graphics.newImage('graphics/object.png')

    self.width = self.image:getWidth()
    self.height = self.image:getHeight()

    self.x = (VIRTUAL_WIDTH - self.width) / 2
    self.y = (VIRTUAL_HEIGHT - self.height) / 2

    self.center_x = self.x + self.width/2
    self.center_y = self.y + self.height/2
    
    self.mass = 100   
end

function Celestial:update(dt)
    
end



function Celestial:render()
    love.graphics.draw(self.image, self.x, self.y, 0)
end