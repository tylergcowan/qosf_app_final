
import PIL.Image as Image
import io

with open("trythis - Copy.jpg", "rb") as image:
    f = image.read()
    b = bytearray(f)
    print(len(b))

bi=[]
i=0
for xx in b:
    bi.append(format(b[i],'08b'))  # GOAL OF THIS IS TO CONVERT FROM SAY, 216, TO LIKE 10010110
    i+=1

# this is how you'll do it. use this to convert
c=[]
for x in bi:
    c.append(int(x,2))
c=bytearray(c)


# use this
#image2 = Image.open(io.BytesIO(c))
#image2.save("testt123t123t.jpg")


final_b=[]

# split this into groups of 4, then send
i=0
# the array of 4 bytes to process
process=[]
for val in bi:
    process.append(bytes(val,'utf-8'))
    i+=1
    if i==4:# send it pieces of 4 bytes
        i=0
        #print(process)
        #now process the 4?
        for x in process:
            #print(type(bytes(x,'utf-8')))
            final_b.append(x)
#            final_b.append(bytes(x,'utf-8'))
        process=[]

print(type(final_b))

i=0
for xy in final_b:
    final_b[i]=final_b[i].encode('utf-8')
    i+=1


image2 = Image.open(io.BytesIO(final_b))
image2.save("testttt.jpg")



'''
j=0
for i in final_b:
    if(final_b[j]!=bi[j])
    j+=1

print(final_b==bi)
'''






