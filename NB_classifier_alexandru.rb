require 'rubygems' 
require 'stuff-classifier' 
require 'spreadsheet'

wine = StuffClassifier::TfIdf.new("wine")
rating = {'0' => :no, '1' => :yes, '2' =>:maybe}
wine.ignore_words = File.readlines('stopwords')

txtfiles = File.readlines('alcohol_MC.txt')
txtfiles.each do |spread|
     book = Spreadsheet.open spread;
     sheet1 = book.worksheet 0
     sheet1.each do |row|
          if !row[1].nil?
               wine.train(rating[row[1].to_i.to_s],row[0])
          end
     end
end
puts wine.classify(' being able to talk to my manager about boys and alcohol')
puts wine.classify(' 80party  party  awesomeness  citylife  ohshit  alcohol  drinking  smile http   t co tq6pgur2qn')
puts wine.classify(' i think alcohol is still in my system')


 

     