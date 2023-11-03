require 'src/Dependencies'

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243
-- VIRTUAL_HEIGHT = 432

background = love.graphics.newImage('graphics/background.png')

function love.load()
    love.graphics.setDefaultFilter('nearest', 'nearest')

    love.window.setTitle('game-1')

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        vsync = true,
        fullscreen = false,
        resizable = true
    })

    gStateMachine = StateMachine {
        ['play'] = function() return PlayState() end
    }
    gStateMachine:change('play', {})

    love.keyboard.keysPressed = {}
end


function love.update(dt)
    gStateMachine:update(dt)

    love.keyboard.keysPressed = {}
end


function love.draw()
    push:apply('start')
    
    local backgroundWidth = background:getWidth()
    local backgroundHeight = background:getHeight()
    love.graphics.draw(background, 0, 0, 0, 
    VIRTUAL_WIDTH / (backgroundWidth - 1), VIRTUAL_HEIGHT / (backgroundHeight - 1))

    gStateMachine:render()

    push:apply('end')
end


function love.resize(w, h)
    push:resize(w, h)
end


function love.keypressed(key)
    love.keyboard.keysPressed[key] = true
end


function love.keyboard.wasPressed(key)
    if love.keyboard.keysPressed[key] then
        return true
    else
        return false
    end
end


