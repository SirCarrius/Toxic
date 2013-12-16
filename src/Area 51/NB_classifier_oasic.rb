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

#
tokens = "I am drinking beer right now".split(/\s+/)
result = alcohol.classify(tokens)
#

yesstates = Hash.new(0)
totalstates = Hash.new(0)
nostates = Hash.new(0)
maybestates = Hash.new(0)
totalcount = 0
yescount = 0
counter =0

File.open("alcohol_geo_yes.txt",'w') do |y|
File.open("alcohol_geo_no.txt",'w') do |n|
File.open("alcohol_geo_maybe.txt",'w') do |m|

to_classify_files = File.read('toclassify.txt').split('|')
to_classify_files.each do |txt|
     to_classify_file = File.readlines("positive-control.txt")
     to_classify_file.each do |line|
          totalcount +=1
          a = line.split('|')
          tokens = a[2].split(/\s+/)
          cls = alcohol.classify(tokens)
          if cls.max_class.to_s == 'yes'
               y.puts a[1] + "|" + a[2]
               yescount += 1
               yesstates[a[0]]+=1
               totalstates[a[0]]+=1
          end
          if cls.max_class.to_s == 'no'
               n.puts a[1] + "|" + a[2]
               nostates[a[0]]+=1
               totalstates[a[0]]+=1
          end
          if cls.max_class.to_s == 'maybe'
               m.puts a[1] + "|" + a[2]
               maybestates[a[0]]+=1
               totalstates[a[0]]+=1          
          end
     counter = counter +1
     end
end
#end of File opens
end
end
end

#classify the null query
nullyesstates = Hash.new(0)
nulltotalstates = Hash.new(0)
nulltotal=0
yesnull=0
clnull = File.readlines('null_geo.txt')
clnull.each do |null|
     nulltotal +=1
     a = null.split('|')
     tokens = a[2].split(/\s+/)
     ncls = alcohol.classify(tokens)
     if ncls.max_class.to_s == 'yes'
          yesnull += 1
          nullyesstates[a[0]]+=1
          nulltotalstates[a[0]]+=1
     end
     if ncls.max_class.to_s == 'no'
          nulltotalstates[a[0]]+=1
     end
     if ncls.max_class.to_s == 'maybe'
          nulltotalstates[a[0]]+=1          
     end
               
end

#location quotient
lq = Hash.new(0.0)
yesstates.each do |key,value|
     if !nulltotalstates.has_key?(key)
         nulltotalstates[key] = 1
         nullyesstates[key] = 1
     end
     if !nullyesstates.has_key?(key)
          nullyesstates[key]=nulltotalstates[key]
     end
     lq[key]=((yesstates[key]*1.0)/totalstates[key])/((nullyesstates[key]*1.0)/nulltotalstates[key])
end

puts lq
puts yesstates["test"]

File.open('location_quotient.txt','w') do |l|
     l.puts lq
end