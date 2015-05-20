
# marking rubric: https://www.udacity.com/course/viewer/#!/c-nd000/l-3568138824/m-3647198607

'''
EXAMPLE INPUT:
'''

block = '''
TITLE: Solving Problems
DESCRIPTION: Programming problems can be solved by 
breaking problems into smaller pieces, 
precisely and mechanically describing a series of steps that may be used to solve each piece, and 
those steps can be executed by a computer.
TITLE: Terminology
DESCRIPTION: Machines can only perform functions for which they were designed, and a computer is a machine that can do any computation. A program 
tells a computer what to do in a precise sequence of steps. A program written in a 
high-level language such as Python is interpreted by that language, and fed to the computer in 
a way the computer understands. A program's input is what it takes in, and its output is what results, 
an interpreter is a program that takes code as input, and outputs machine-readable 
instructions.
TITLE: Variables
DESCRIPTION: A variable is a way of storing data. In Python data is stored (assigned) using the "=" symbol. 
Assignment is not math - it does something and assigns the data to the variable, it doesn't simply 
describe something that it true.
TITLE: Functions
DESCRIPTION: A function is a mini-program. It takes input, does something with it, and generates output. 
Functions are useful because they are bits of code that may be re-used a number of times during your program without 
the need to re-write the code each time. Also, this allows following the DRY principle. With no return statement, 
a function evaluates to None in Python. You make a function with ""def", you use a function by calling it. In making a function, 
you have to be prepared for (theoretically) any input; when you call the function, you may know what input you are passing in. This 
makes the "assert" statement very useful to validate the type of data you are receiving.
TITLE: Control Flow and Loops
DESCRIPTION: Allows the program to make decisions and selectively run certain pieces of code, either 
over and over, or not at all.
TITLE: Debugging
DESCRIPTION: We went over 5 debugging strategies in this lesson: (1) Examine error messages when programs crash: The last line of Python Tracebacks will tell you what went wrong. Reading backwards from there will tell you more about where the problem occurred.
(2) Work from example code: If your modified code doesn't work, comment it out and do step-by-step modifications to the example code until it does what you want.
(3) Make sure examples work: Just because you find example code doesn't mean it will work in your system. Check the example code you're using to make sure it behaves the way you expect.
(4) Check (print) intermediate results: When your code doesn't crash, but doesn't behave as expected, add print statements to your program to see where in the code things stop behaving correctly.
(5) Keep and compare old versions: When you have a working version of your code, save it before you add to the code. This will give you something to go back to if you introduce too many new bugs.
TITLE: Structured Data and For Loops
DESCRIPTION: (1) Mutation: change data in place, as opposed to creating a new object
(2) Aliasing: when an object is assigned to more than one variable names, each variable name modifies that same object (i.e. the same object can have multiple names)
(3) Structured data:  data which is held in objects that give the data structure -- eg. lists, tuples, dictionaries, etc.
(4) Mutability: data that is mutable can be changed in-place, immutable data cannot be changed, and must be used in new objects.
(5) The difference between append and +:  both add an item to create a different list - append mutates, and "+" creates a new list.
TITLE: How to Solve Problems
DESCRIPTION: First: make sure you understand the problem. The problem is defined by the relationship between the inputs and outputs -- eg. what goes in the black box? 
1) DON'T PANIC 
2) What are the inputs? (Defensive programming -- test to make sure assumptions are  [use "assert <expression>"; returns False if assertion fails]) 
3) What are the outputs? 
4) Work through examples by hand 
4a) Create some test cases: give input as taken by the function, and the output, and build-in exceptions 
4b) Understand how to solve the test cases in a systematic way, as a human 
5) Begin creating a simple mechanical solution -- the necessity for fast code is determined by the expected use of the code (eg. number of times it will be run) 
5a) Write PseudoCode -- don't start writing actual code until the code is (1) simple, and (2) handles almost all cases... there is a nexus between simplicity and 
cases that the code handles that must be reached before writing code. Simple == more likely to be correct 
5b) Begin writing small bits of code with simplifications, and testing them as you go -- write the easy bits first, making assumptions as necessary (eg. assume each month has 30 days) 
6) Develop the solution incrementally in small steps
'''

'''TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of 
the loop until the "test condition" is no longer true.'''

def make_array(text):
	# assert type(text) == StringType
	text = text.replace("\n", "") # remove newlines from input
	array = []
	title_pos = 0 #set variable which will be used as (1) position of the start of the string "TITLE:", and the beginning of the search for the next "TITLE:" at various points
	while title_pos != -1: #run loop while "TITLE" is found
		# print "__TITLE_POS:__" + str(title_pos) # debugging line
		descr_pos = text.find("DESCRIPTION:", title_pos) #find start of word DESCRIPTION
		# print "__DESCR_POS:__" + str(descr_pos) # debugging line
		titleText = text[title_pos+7:descr_pos] #store title text, and remove the leading space
		title_pos = descr_pos #set beginning position of next searches (for description)
		descrText = text[descr_pos+13:text.find("TITLE:", title_pos)] #store description text, and remove the leading space
		# print "__TITLETEXT:__" + str(titleText) # debugging line
		# print "__DESCRTEXT:__" + str(descrText) # debugging line
		array.append([titleText, descrText]) #adds title and description to array (which is eventually returned)
		title_pos = text.find("TITLE:", title_pos) #find start of word TITLE for next iteration
	# print "__ARRAY:__" + str(array) # debugging line
	return array # returns an array with the format [[title1, descr1],[title2, descr2],etc.]

structured_text = make_array(block)	#turn the string into a structured set of data
# print str(structured_text) # debugging line

def write_html(info, headingLevel=2): #takes an array with the structure [[title1, descr1],[title2, descr2],etc.] and turn it into HTML, with each title as a heading of headinglevel, and a linked table of contents
	TOC = ""
	body = ""
	textReturn = ""
	TOC = '''<nav role = "navigation" class = "TOC">
			<h1>Main Topics</h1>
				<ul>'''
	for x in info: #write TOC
		TOC += '<li><a href = "#%s">%s</a></li>' % (x[0].replace(" ","%20"),x[0]) # put %20 instead of spaces in links
	TOC += '''		</ul>
		</nav>'''
		
	body += '''<div class = "info">
	<div class = "content">''' #open info and content divs
	for x in info: #write body text
		body += '''
			<div class = "body">
				<h%s id = "%s">%s</h%s>
					<p>%s</p>
			</div>
		''' % (headingLevel, x[0].replace(" ","%20"), x[0], headingLevel, x[1]) #write each heading and body text
	
	body += '''</div>
	 </div>''' # close info and content divs
			
	textReturn = TOC + '\n' + body # concatenate TOC and body
	return textReturn #return HTML
	

print write_html(structured_text,2) #print HTML
	


'''EXAMPLE OUTPUT:
<div class="concept">
    <div class="concept-title">
        Why Computers are Stupid
    </div>
    <div class="concept-description">
	The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.

    </div>
</div>
<div class="concept">
    <div class="concept-title">
        Python
    </div>
    <div class="concept-description">
        Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.

    </div>
</div>
<div class="concept">
    <div class="concept-title">
        While Loops
    </div>
    <div class="concept-description">
        A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true.
    </div>
</div>'''