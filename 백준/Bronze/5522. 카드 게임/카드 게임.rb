# sum = 0
# (1..5).times do
#   sum += gets.chomp.to_i
# end
# puts sum

# puts (1..5).inject(0) { |sum, _| sum + gets.chomp.to_i }
# # _ 는 루프변수. 사용하지 않으므로 언더바 처리

puts (1..5).map { gets.chomp.to_i }.sum