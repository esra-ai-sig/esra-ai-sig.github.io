require 'jekyll'
require 'time'
source = File.read('_includes/event-state.html')
template = Liquid::Template.parse(source)
cases = [
  ['launch day', '2026-10-22', {'date'=>'2026-10-22'}, 'Today'],
  ['after launch', '2026-10-23', {'date'=>'2026-10-22'}, 'Past'],
  ['future course', '2026-10-22', {'date'=>'2026-11-05','end_date'=>'2026-11-19'}, 'Upcoming'],
  ['course underway', '2026-11-12', {'date'=>'2026-11-05','end_date'=>'2026-11-19'}, 'In progress'],
  ['last course day', '2026-11-19', {'date'=>'2026-11-05','end_date'=>'2026-11-19'}, 'In progress'],
  ['after series', '2026-11-20', {'date'=>'2026-11-05','end_date'=>'2026-11-19'}, 'Past'],
  ['announced webinar', '2026-10-22', {'month'=>'2026-11'}, 'Announced'],
  ['stale announcement', '2026-12-01', {'month'=>'2026-11'}, 'Awaiting an update'],
  ['unapproved training', '2026-10-22', {'status'=>'pending'}, 'Pending approval'],
  ['accepted session', '2026-10-22', {'date'=>'2027-07-19','end_date'=>'2027-07-23','status'=>'accepted'}, 'Accepted session'],
  ['past session', '2027-07-24', {'date'=>'2027-07-19','end_date'=>'2027-07-23','status'=>'accepted'}, 'Past']
]
cases.each do |name, day, event, expected|
  actual=template.render!({'site'=>{'time'=>Time.parse(day)},'include'=>{'event'=>event}}).strip
  abort "FAIL #{name}: #{actual.inspect} != #{expected.inspect}" unless actual==expected
end
puts "PASS: #{cases.length} event date/status boundaries"
