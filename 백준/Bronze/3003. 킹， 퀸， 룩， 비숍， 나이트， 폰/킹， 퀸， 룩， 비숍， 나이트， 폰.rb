# set = [1,1,2,2,2,8]
# input = gets.split.map(&:to_i)
# result = []

# (0..5).each do |i|
#   result << (set[i] - input[i])
# end

# puts result.join(" ")

set = [1,1,2,2,2,8]
input = gets.split.map(&:to_i)

result = set.map.with_index { |value, i| value - input[i] }
puts result.join(" ")
