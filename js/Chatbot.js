var known = [
				["hello", "hi"],
				["i am *", "are you *?"],
				["say * please", "*"],
				["say *", "say please"],
			];

			var input = document.querySelector('input');
			var output = document.querySelector('div');

			function postChat(text, poster) {
				var bubble = document.createElement("p");
				bubble.innerText = text;
				bubble.className = poster;
				output.appendChild(bubble);
			}

			function respond() {
				var text = input.value;
				input.value = "";
				postChat(text, "user");
				var response = think(text);
				postChat(response, "bot");
			}

			function filter(text) {
				text = text.toLowerCase();
				return(text);
			}

			function think(user) {
				user = filter(user);

				for (var [key, value] of known) {
					if (key.includes('*')) {
						key = key.split('*');

						if (user.startsWith(key[0]) && user.endsWith(key[1])) {
							var firstIndex = key[0].length;
							var finalIndex = user.lastIndexOf(key[1]);
							var custom = user.slice(firstIndex, finalIndex);
							return(value.replace('*', custom));
						}
					} else if (user == key) {
						return(value);
					}
				}
				return("What?");
			}