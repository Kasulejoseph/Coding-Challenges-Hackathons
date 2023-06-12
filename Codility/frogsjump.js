function solution(blocks) {
  const n = blocks.length;
  const maxJumpsRight = Array(n).fill(0);
  const maxJumpsLeft = Array(n).fill(1);

  // build right jumps array
  for (let i = 0; i < n; i++) {
    const currentBlock = blocks[i];
    const previousBlock = blocks[i - 1];

    if (i !== 0 && currentBlock <= previousBlock) {
      maxJumpsRight[i] = maxJumpsRight[i - 1] + 1;
    }
  }

  // build left jumps array
  for (let i = n; i > 0; i--) {
    const currentBlock = blocks[i - 1];
    if (i !== n && currentBlock <= blocks[i]) {
      maxJumpsLeft[i - 1] = maxJumpsLeft[i] + maxJumpsLeft[i - 1];
    }
  }
  console.log(maxJumpsRight, maxJumpsLeft);

  let maxDistance = 0;
  
  // max distance between the two frogs
  for (let i = 0; i < n; i++) {
    const distance = maxJumpsLeft[i] + maxJumpsRight[i];
    if (distance > maxDistance) {
      maxDistance = distance;
    }
  }
  return maxDistance;
}

solution([1, 1]);
