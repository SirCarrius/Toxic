require 'rubygems' 
require 'stuff-classifier' 
require 'spreadsheet'

#Initialize classifier
store = StuffClassifier::FileStorage.new("classifier.db")
toxifier = StuffClassifier::TfIdf.new("tox", :storage => store)
toxifier.ignore_words = File.readlines('stopwords')

#Rating scheme
rating = {'0' => :no, '1' => :yes, '2' =>:maybe}

#Train classifier by reading in curated data
filename = 'alcohol_MC.xls'
book= Spreadsheet.open filename
sheet = book.worksheet 0 

sheet.each do |row|
	unless row[1].nil?
		toxifier.train(rating[row[1].to_i.to_s],row[0])
	end
end

#Persist classifier on database
toxifier.save_state

 

     