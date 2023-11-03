PlayState = Class{__includes = BaseState}

function PlayState:init()
    self.satellite = Satellite()
    self.celestial = Celestial()

    self.gravity = 3 

end


function PlayState:update(dt)
    self.distance_x = self.satellite.center_x - self.celestial.center_x + 0.1
    self.distance_y = self.satellite.center_y - self.celestial.center_y + 0.1
    self.hypotenuse = math.sqrt(self.distance_x^2 + self.distance_y^2)
    
    self.gravitational_F = (self.gravity * self.celestial.mass * self.satellite.mass) / self.hypotenuse^2

    self.accel_x = -(self.gravitational_F * math.cos(math.rad(self.distance_x/self.hypotenuse)))
    self.accel_y = -(self.gravitational_F * math.sin(math.rad(self.distance_y/self.hypotenuse)))
    self.force_check = math.sqrt(self.accel_x^2 + self.accel_y^2)
    
    if self.distance_x > 0 then
        self.accel_x = -self.accel_x
    end
    self.satellite.accel_x = self.accel_x
    self.satellite.accel_y = self.accel_y

    self.satellite:update(dt)

    if love.keyboard.wasPressed('escape') then
        love.event.quit()
    end
end


function PlayState:render()
    self.satellite:render()
    self.celestial:render()

    love.graphics.print("x:"..string.format("%.2f", self.distance_x), 0, 0)
    love.graphics.print("y:"..string.format("%.2f", self.distance_y), 0, 16)
    love.graphics.print("hy:"..string.format("%.2f", self.hypotenuse), 0, 32)
    love.graphics.print("F_g:"..string.format("%.2f", self.gravitational_F), 0, 48)
    love.graphics.print("F_c:"..string.format("%.6f", self.force_check), 0, 64)



    
end