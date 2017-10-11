## Regular expression

### Concept:

A regular expression, commonly called a “regexp”, is a sequence of characters that define a search pattern.  It is mainly for use in pattern matching with strings, or string matching (i.e. it operates like a “find and replace” command). While it is a very powerful tool, it is also very dangerous because of its complexity.

Regular Expressions: Now You Have Two Problems

Some people, when confronted with a problem, think [“I know, I’ll use regular expressions.”   Now they have two problems](http://regex.info/blog/2006-09-15/247). (super classic joke in the industry)

One thing you have to be careful with is that different languages use different regexp engines. That means that a regexp in Python, for example, will be interpreted differently in Javascript:

Regular expressions are everywhere and software engineers, no matter their positions, will have to use them during their careers. System administrators and DevOps are the one using them the most because they are very handy for log parsing.

Read about regexp:

- [http://www.regular-expressions.info/](https://intranet.hbtn.io/rltoken/UiNlZh3kfbxisotXH-gI0A)
- [http://www.w3schools.com/jsref/jsref_obj_regexp.asp](https://intranet.hbtn.io/rltoken/tcX5DBSbWv1emQQQIzuchw) Play with regexp (or compose them):

- Ruby: [http://rubular.com/](https://intranet.hbtn.io/rltoken/M4whgZsxtYEk50WGcYbPRA)

- PHP/Javascript/Python: [https://regex101.com/](https://intranet.hbtn.io/rltoken/InqFxs9vWK2lTXxeCVHM8Q)

### Read

- [Regular expressions - basics](https://intranet.hbtn.io/rltoken/SJ2eQ7V2iQlCgLc-L96zWg)
- [Regular expressions - advanced](https://intranet.hbtn.io/rltoken/qyjWL-J1_qUaZGR690gH1Q)
- Your best friend for this project is [http://rubular.com/](https://intranet.hbtn.io/rltoken/7Ov55GiGyxQ8z7-CiUuLew)
- Understand a famous developer joke: “Use a regular expression against a problem: [now you have 2 problems](https://intranet.hbtn.io/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw)”
- Learn by doing with [https://www.regexone.com/](https://intranet.hbtn.io/rltoken/1-Hca1vIUt-busoFAr3kgQ)

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries have sometimes different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in beetween the //:
```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

### Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
- All your regex must be built for the Oniguruma library
