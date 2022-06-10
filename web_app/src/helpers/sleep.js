function timeout(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
export async function sleep(fn, ms, ...args) {
  await timeout(ms);
  return fn(...args);
}
