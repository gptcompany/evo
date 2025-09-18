import { defineConfig } from 'vitest/config'
import { VitestReporter } from 'tdd-guard-vitest'

export default defineConfig({
  test: {
    reporters: [
      'default',
      new VitestReporter('/home/sam/EVO'),
    ],
    include: ['**/*.{test,spec}.{js,mjs,cjs,ts,mts,cts,jsx,tsx}'],
    exclude: ['node_modules', 'dist', '.venv'],
  },
})