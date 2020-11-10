#!/usr/bin/env ruby
regex2 = ARGV[0]
puts regex2.scan(/^\d{10}$/).join
