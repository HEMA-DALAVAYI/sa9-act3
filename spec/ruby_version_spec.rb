require 'ruby_version'

RSpec.describe Dog do
  describe "#set_color" do
    it "is an instance variable that sets color" do
      roger = Dog.new('pug')
      roger.set_color('Blue')
      expect(roger.get_color).to eq('Blue')
    end
  end

  describe "#to_s" do
    it "is is like the string method in python where when you call the object with the info nicely displayed" do
      sue = Dog.new('lab')
      sue.set_color('Pink')
      expect(sue.to_s).to eq("breed: lab, color: Pink")
    end
  end
end
