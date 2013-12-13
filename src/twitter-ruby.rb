#1/usr/bin/ruby

require 'rubygems'
require 'json'
#require 'ap' 
require 'twitter'
require 'optparse'

options = {}
optparse = OptionParser.new do |opt|
    #Banner
    opt.banner = "Usage: ruby twitter-ruby.rb -d drug -o output"

    opt.on("-d drug") do |drug|
        options[:drug] = drug  || nil 
        options[:output] = drug +"_out"
    end

    opt.on("-o output") do |output|
        options[:output] = output
    end

    opt.on_tail('-h') do
        puts opt.banner
    end
end

begin
    optparse.parse!
    puts optparse.banner if not options[:drug] 
end

if options[:drug] and options[:output]
    tokens = JSON.load(IO.read('tokens.json'))['twitter']
    Twitter.configure do |config|
    	config.consumer_key = tokens['consumer-key']
    	config.consumer_secret = tokens['consumer-secret']
    	config.oauth_token = tokens['oauth-token']
    	config.oauth_token_secret = tokens['oauth-secret']
    end

    puts "Searching for #{options[:drug]}"
    puts "Saving output to #{options[:output]}.txt"

    File.open(options[:output]+'.txt','a') do |s|
        10.times do |d|
            id = 0
            Twitter.search(options[:drug], :count => 100, :max_id => id).results.map do |status|
                body = status.text.gsub(/\W/,' ').strip.downcase
                target = status.from_user.downcase
                s.puts "#{target} | #{body}"
                id = status.from_user_id
            end
        end
    end
end