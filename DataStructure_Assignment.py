{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['kathak', 'bharatnatyam', 'kathakali', 'Orissi', 'kucchipudi']\n"
     ]
    }
   ],
   "source": [
    "dances = ['kathak','bharatnatyam','kathakali','Orissi']\n",
    "dances.append('kucchipudi')\n",
    "print(dances)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "english\n"
     ]
    }
   ],
   "source": [
    "myTuple = ('hindi','english','french','spanish','sanskrit')\n",
    "print(myTuple[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sanskrit\n"
     ]
    }
   ],
   "source": [
    "print(myTuple[4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'book': 'Rich Dad Poor Dad', 'author': 'Robert Kiyosaki', 'edition': '2000', 'price': '250'}\n"
     ]
    }
   ],
   "source": [
    "myDict = {\"book\":\"Rich Dad Poor Dad\",\n",
    "         \"author\":\"Robert Kiyosaki\",\n",
    "         \"edition\":\"2000\",\n",
    "         \"price\":\"250\"}\n",
    "print(myDict)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2000\n"
     ]
    }
   ],
   "source": [
    "print(myDict[\"edition\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'book': 'Rich Dad Poor Dad', 'author': 'Robert Kiyosaki', 'price': '250'}\n"
     ]
    }
   ],
   "source": [
    "myDict.pop(\"edition\")\n",
    "print(myDict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
