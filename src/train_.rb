require 'nbayes'
require 'spreadsheet'

alcohol = NBayes::Base.new


rating = {'0' => :no, '1' => :yes, '2' =>:maybe}
#classifiers.txt contains the SUBSTANCE_geo.txt files delimited by |
txtfiles = File.read('classifiers.txt').split('|')
txtfiles.each do |spread|
     book = Spreadsheet.open spread;
     sheet1 = book.worksheet 0
     sheet1.each do |row|
          if !row[1].nil?
               alcohol.train(row[0].split(/\s+/),rating[row[1].to_i.to_s])
          end
     end
end

alcohol.dump('classifier.nb')