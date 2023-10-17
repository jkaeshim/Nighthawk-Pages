{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "\n",
    "app = Flask(__name__)\n",
    "data = []  # This will store our data\n",
    "\n",
    "@app.route('/api/data', methods=['GET'])\n",
    "def get_data():\n",
    "    return jsonify(data)\n",
    "\n",
    "@app.route('/api/data', methods=['POST'])\n",
    "def add_data():\n",
    "    new_data = request.get_json()\n",
    "    data.append(new_data)\n",
    "    return jsonify({\"message\": \"Data added successfully\"}), 201\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
