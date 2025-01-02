import endpoint from "./configTypes"
import { test, expect } from '@playwright/test'

test("Expect to have 3 options for signing up", async ({ page }) => {

  // Go to the Droplets product page of DigitalOcean web page
  await page.goto(endpoint.BASE_URL);

  // Wait for the page to load
  await page.waitForLoadState('networkidle');

  // Get the number of signUp options
  const number_subscriptions_allowed = await page.locator('.SignupButtonsStyles__ButtonContainer-sc-yg5bly-0 > a').count()

  // Verify that number equals 3
  expect(number_subscriptions_allowed).toBe(3)
});
