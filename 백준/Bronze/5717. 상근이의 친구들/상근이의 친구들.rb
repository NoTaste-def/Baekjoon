# while line = gets
#   boy, girl = line.split.map(&:to_i)
#   break if boy == 0 && girl == 0
#   puts boy+girl
# end

ARGF.each_line do |line|
  boy, girl = line.split.map(&:to_i)
  break if boy == 0 && girl == 0
  puts boy+girl
end