class Dog
  def initialize(breed)
      @breed = breed
  end

  def set_color(color)
    @color = color
  end

  def get_color
    @color
  end

  def to_s
    "breed: #{@breed}, color: #{@color}"
  end

end


'''
# create the objects
roger = Dog.new('pug')
sue = Dog.new('lab')

# setting the color of the objects through the method setColor
roger.set_color('green')
sue.set_color('pink')


puts roger.get_color
puts sue.get_color
puts
puts roger
puts sue
'''
