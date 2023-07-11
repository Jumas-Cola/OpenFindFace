import { describe, it, expect, vi } from 'vitest';
import { mount } from '@vue/test-utils';
import { useI18n } from 'vue-i18n';

import FaceCardItem from '../face/FaceCardItem.vue';

vi.mock('vue-i18n');

useI18n.mockReturnValue({
  t: (tKey: string) => tKey
});

describe('FaceCardItem', () => {
  it('renders properly', () => {
    const wrapper = mount(FaceCardItem, {
      props: {
        faceData: {
          name: 'Test Name',
          image: 'test-img'
        }
      }
    });

    expect(wrapper.find('img').element.getAttribute('src')).toBe('/test-img');
    expect(wrapper.text()).toContain('Test Name');
  });
});
