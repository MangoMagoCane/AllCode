PlayState = Class{__includes = BaseState}

function PlayState:init()
    self.player = Player()
end


function PlayState:update(dt)
    self.player:update(dt)

    if love.keyboard.wasPressed('escape') then
        love.event.quit()
    end
end


function PlayState:render()
    self.player:render()
end