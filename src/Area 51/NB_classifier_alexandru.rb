require 'rubygems' 
require 'stuff-classifier' 
require 'spreadsheet'

toxifier = StuffClassifier::TfIdf.new("tox")
rating = {'0' => :no, '1' => :yes, '2' =>:maybe}
toxifier.ignore_words = File.readlines('stopwords')

curated_data = File.readlines('alcohol_MC.txt')
curated_data.each do |spread|
     book = Spreadsheet.open spread;
     sheet1 = book.worksheet 0
     sheet1.each do |row|
          if !row[1].nil?
               toxifier.train(rating[row[1].to_i.to_s],row[0])
          end
     end
end

puts toxifier.classify(' being able to talk to my manager about boys and alcohol')
puts toxifier.classify(' 80party  party  awesomeness  citylife  ohshit  alcohol  drinking  smile http   t co tq6pgur2qn')
puts toxifier.classify(' i think alcohol is still in my system')


 

     